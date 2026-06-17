// Global State
let videos = [];
let activeVideo = null;
let currentCategory = 'all';
let searchQuery = '';

// DOM Elements
const videosGrid = document.getElementById('videos-grid');
const mainVideo = document.getElementById('main-video');
const playerPlaceholder = document.getElementById('player-placeholder');
const activeTitle = document.getElementById('active-title');
const activeDescription = document.getElementById('active-description');
const activeTags = document.getElementById('active-tags');
const activeSize = document.getElementById('active-size');
const activeDate = document.getElementById('active-date');
const copyLinkBtn = document.getElementById('copy-link-btn');
const copyToast = document.getElementById('copy-toast');
const searchInput = document.getElementById('search-input');
const clearSearchBtn = document.getElementById('clear-search');
const filterTabs = document.getElementById('filter-tabs');

// Modal Elements
const helpBtn = document.getElementById('help-btn');
const helpModal = document.getElementById('help-modal');
const closeModalBtn = document.getElementById('close-modal-btn');

const adminBtn = document.getElementById('admin-btn');
const adminModal = document.getElementById('admin-modal');
const closeAdminBtn = document.getElementById('close-admin-btn');
const adminVideoList = document.getElementById('admin-video-list');

// Initialize App
document.addEventListener('DOMContentLoaded', () => {
  fetchVideos();
  setupEventListeners();
});

// Event Listeners Setup
function setupEventListeners() {
  // Search input typing
  searchInput.addEventListener('input', (e) => {
    searchQuery = e.target.value.toLowerCase().trim();
    if (searchQuery.length > 0) {
      clearSearchBtn.classList.remove('hidden');
    } else {
      clearSearchBtn.classList.add('hidden');
    }
    renderGrid();
  });

  // Clear search button
  clearSearchBtn.addEventListener('click', () => {
    searchInput.value = '';
    searchQuery = '';
    clearSearchBtn.classList.add('hidden');
    renderGrid();
  });

  // Category filter tabs
  filterTabs.addEventListener('click', (e) => {
    const tab = e.target.closest('.filter-tab');
    if (!tab) return;

    // Toggle active tab class
    document.querySelectorAll('.filter-tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');

    currentCategory = tab.dataset.category;
    renderGrid();
  });

  // Copy shareable link
  copyLinkBtn.addEventListener('click', () => {
    if (!activeVideo) return;
    
    // Create shareable link pointing to this video using query parameters
    const baseUrl = window.location.origin + window.location.pathname;
    const shareUrl = `${baseUrl}?video=${encodeURIComponent(activeVideo.filename)}`;

    navigator.clipboard.writeText(shareUrl)
      .then(() => {
        copyToast.classList.remove('hidden');
        setTimeout(() => {
          copyToast.classList.add('hidden');
        }, 2500);
      })
      .catch(err => {
        console.error('Could not copy link: ', err);
      });
  });

  // Modal Open/Close
  helpBtn.addEventListener('click', () => helpModal.classList.remove('hidden'));
  closeModalBtn.addEventListener('click', () => helpModal.classList.add('hidden'));
  
  // Close modal when clicking outside content area
  helpModal.addEventListener('click', (e) => {
    if (e.target === helpModal) {
      helpModal.classList.add('hidden');
    }
  });

  // Admin Modal Open/Close
  adminBtn.addEventListener('click', () => {
    adminModal.classList.remove('hidden');
    renderAdminList();
  });
  closeAdminBtn.addEventListener('click', () => adminModal.classList.add('hidden'));
  adminModal.addEventListener('click', (e) => {
    if (e.target === adminModal) {
      adminModal.classList.add('hidden');
    }
  });

  // Handle ESC key to close modal
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      helpModal.classList.add('hidden');
      adminModal.classList.add('hidden');
    }
  });

  // Show admin button only if hosted locally
  const isLocal = window.location.hostname === 'localhost' || 
                  window.location.hostname === '127.0.0.1' || 
                  window.location.hostname.startsWith('192.168.') ||
                  window.location.hostname.startsWith('10.');
  if (isLocal) {
    adminBtn.classList.remove('hidden');
  }
}

// Fetch video list
async function fetchVideos() {
  try {
    // Try fetching from the local server's dynamic API endpoint first
    let response = await fetch('/api/videos');
    
    // If that fails (e.g. 404 on static hosting), fall back to fetching the static JSON file
    if (!response.ok) {
      console.warn('Backend API endpoint not available. Falling back to static videos.json.');
      response = await fetch('videos.json');
    }
    
    videos = await response.json();
    
    if (videos && videos.length > 0) {
      renderGrid();
      handleDeepLink();
    } else {
      renderEmptyState("No Videos Found", "No video files found in the directory. Please add MP4 videos to E:\\Demos.");
    }
  } catch (error) {
    console.error('Error loading video data:', error);
    // If fetching videos.json fails, try to render an error state
    renderEmptyState("Error Loading Showcase", "Could not fetch the video database. If hosting on GitHub Pages, make sure public/videos.json is pushed.");
  }
}

// Check for deep links in URL query params
function handleDeepLink() {
  const urlParams = new URLSearchParams(window.location.search);
  const videoParam = urlParams.get('video');
  
  if (videoParam) {
    const videoName = decodeURIComponent(videoParam);
    const video = videos.find(v => v.filename === videoName);
    if (video) {
      selectVideo(video, false); // select and scroll, do not auto-scroll if unwanted, but we do smooth scrolling
      
      // Smooth scroll to player on load if deep linked
      const playerElement = document.querySelector('.hero-showcase');
      if (playerElement) {
        playerElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }
  }
}

// Convert OneDrive and Google Drive share URLs to direct streaming/download URLs
function getDirectVideoUrl(videoObj) {
  // If we have an onlineUrl set, prioritize it; otherwise use localUrl
  const url = videoObj.onlineUrl && videoObj.onlineUrl.trim() !== "" ? videoObj.onlineUrl : videoObj.localUrl;
  
  if (!url) return '';
  if (!url.startsWith('http')) return url; // Relative local path (e.g. "videos/MyVideo.mp4")

  // 1. Google Drive direct stream url conversion
  if (url.includes('drive.google.com')) {
    let fileId = '';
    // Formats:
    // https://drive.google.com/file/d/FILE_ID/view?usp=sharing
    // https://drive.google.com/open?id=FILE_ID
    const matches = url.match(/\/file\/d\/([a-zA-Z0-9_-]+)/);
    if (matches && matches[1]) {
      fileId = matches[1];
    } else {
      const idParam = url.match(/[?&]id=([a-zA-Z0-9_-]+)/);
      if (idParam && idParam[1]) {
        fileId = idParam[1];
      }
    }
    if (fileId) {
      return `https://docs.google.com/uc?export=download&id=${fileId}`;
    }
  }

  // 2. OneDrive direct link conversion
  if (url.includes('onedrive.live.com')) {
    // If it's already an embed link:
    // https://onedrive.live.com/embed?cid=...&resid=...&authkey=...
    // Convert to download link:
    // https://onedrive.live.com/download?cid=...&resid=...&authkey=...
    if (url.includes('/embed')) {
      return url.replace('/embed', '/download');
    }
    // Redirect sharing link:
    if (url.includes('redir?')) {
      return url.replace('redir?', 'download?');
    }
  }

  return url;
}

// Select video and load in main player
function selectVideo(video, shouldScroll = true) {
  activeVideo = video;
  
  // Update UI Elements
  activeTitle.textContent = video.title;
  activeDescription.textContent = video.description;
  
  // Format metadata
  activeSize.innerHTML = `<i class="fa-solid fa-hard-drive"></i> ${formatBytes(video.sizeBytes)}`;
  activeDate.innerHTML = `<i class="fa-solid fa-calendar-days"></i> ${formatDate(video.modifiedAt)}`;
  
  // Tags
  activeTags.innerHTML = '';
  // Category Tag
  const catTag = document.createElement('span');
  catTag.className = `category-tag tag-${video.category.toLowerCase().replace(/\s+/g, '-')}`;
  catTag.textContent = video.category;
  activeTags.appendChild(catTag);
  // Other tags
  if (video.tags && video.tags.length > 0) {
    video.tags.forEach(tag => {
      const span = document.createElement('span');
      span.className = 'category-tag';
      span.style.background = 'rgba(255, 255, 255, 0.03)';
      span.style.color = 'var(--text-secondary)';
      span.style.borderColor = 'var(--card-border)';
      span.textContent = tag;
      activeTags.appendChild(span);
    });
  }

  // Enable copy button
  copyLinkBtn.removeAttribute('disabled');

  // Load and play video
  const streamUrl = getDirectVideoUrl(video);
  mainVideo.src = streamUrl;
  
  // Swap placeholder and video player
  playerPlaceholder.classList.add('hidden');
  mainVideo.classList.remove('hidden');
  
  // Auto-scroll to player if requested (for mobile/tablet experience)
  if (shouldScroll) {
    const playerElement = document.querySelector('.hero-showcase');
    playerElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  // Active status visual feedback on grid
  document.querySelectorAll('.video-card').forEach(card => {
    if (card.dataset.filename === video.filename) {
      card.classList.add('active-card');
      card.style.borderColor = 'var(--accent-blue)';
      card.style.boxShadow = 'var(--glow-blue)';
    } else {
      card.classList.remove('active-card');
      card.style.borderColor = '';
      card.style.boxShadow = '';
    }
  });

  mainVideo.load();
  mainVideo.play().catch(e => {
    console.log('Autoplay was prevented by browser security. User must click play.', e);
  });
}

// Render video grid
function renderGrid() {
  videosGrid.innerHTML = '';
  
  // Filter videos
  const filteredVideos = videos.filter(video => {
    const matchesCategory = currentCategory === 'all' || video.category.toLowerCase() === currentCategory;
    const matchesSearch = video.title.toLowerCase().includes(searchQuery) || 
                          video.description.toLowerCase().includes(searchQuery) ||
                          video.category.toLowerCase().includes(searchQuery) ||
                          video.tags.some(tag => tag.toLowerCase().includes(searchQuery));
    return matchesCategory && matchesSearch;
  });

  if (filteredVideos.length === 0) {
    renderEmptyState("No Matches Found", "Try adjusting your search terms or selecting another category tab.");
    return;
  }

  filteredVideos.forEach(video => {
    const card = document.createElement('div');
    card.className = 'video-card';
    card.dataset.filename = video.filename;
    
    // Add active styling if selected
    if (activeVideo && activeVideo.filename === video.filename) {
      card.classList.add('active-card');
      card.style.borderColor = 'var(--accent-blue)';
      card.style.boxShadow = 'var(--glow-blue)';
    }

    // Get styling category for thumbnail design class
    let categoryClass = 'cover-demos';
    const cat = video.category.toLowerCase();
    if (cat.includes('agentic')) categoryClass = 'cover-agentic-ai';
    else if (cat.includes('optim')) categoryClass = 'cover-optimizers';
    else if (cat.includes('dash')) categoryClass = 'cover-dashboards';

    // Get fontawesome icon based on category
    let categoryIcon = 'fa-solid fa-play';
    if (cat.includes('agentic')) categoryIcon = 'fa-solid fa-robot';
    else if (cat.includes('optim')) categoryIcon = 'fa-solid fa-bolt-lightning';
    else if (cat.includes('dash')) categoryIcon = 'fa-solid fa-chart-line';

    card.innerHTML = `
      <div class="card-thumbnail-wrapper">
        <div class="card-thumbnail-overlay">
          <div class="play-chip">
            <i class="fa-solid fa-play"></i>
          </div>
        </div>
        <!-- Built-in aesthetic vector covers (Zero image placeholders) -->
        <div class="cover-design ${categoryClass}">
          <i class="${categoryIcon} cover-icon"></i>
        </div>
        <div class="card-duration">MP4</div>
      </div>
      <div class="card-content">
        <div class="card-category">${video.category}</div>
        <h3 class="card-title">${video.title}</h3>
        <p class="card-desc">${video.description}</p>
        <div class="card-footer">
          <div class="card-footer-item">
            <i class="fa-solid fa-hard-drive"></i>
            <span>${formatBytes(video.sizeBytes)}</span>
          </div>
          <div class="card-footer-item">
            <i class="fa-solid fa-clock"></i>
            <span>${formatDateShort(video.modifiedAt)}</span>
          </div>
        </div>
      </div>
    `;

    card.addEventListener('click', () => selectVideo(video));
    videosGrid.appendChild(card);
  });
}

// Render empty state helpers
function renderEmptyState(title, description) {
  videosGrid.innerHTML = `
    <div class="empty-state">
      <i class="fa-solid fa-video-slash"></i>
      <h3>${title}</h3>
      <p>${description}</p>
    </div>
  `;
}

// Utility formatting helpers
function formatBytes(bytes) {
  if (!bytes || isNaN(bytes)) return '-- MB';
  const mb = bytes / (1024 * 1024);
  return `${mb.toFixed(2)} MB`;
}

function formatDate(dateString) {
  if (!dateString) return '--';
  const date = new Date(dateString);
  if (isNaN(date.getTime())) return dateString;
  return date.toLocaleDateString('en-US', {
    month: 'long',
    day: 'numeric',
    year: 'numeric'
  });
}

function formatDateShort(dateString) {
  if (!dateString) return '--';
  const date = new Date(dateString);
  if (isNaN(date.getTime())) return dateString;
  return date.toLocaleDateString('en-US', {
    month: 'short',
    year: 'numeric'
  });
}

// Render Admin Panel list
function renderAdminList() {
  adminVideoList.innerHTML = '';
  
  if (videos.length === 0) {
    adminVideoList.innerHTML = '<p style="color: var(--text-muted); text-align: center;">No videos available to manage.</p>';
    return;
  }

  videos.forEach(video => {
    const row = document.createElement('div');
    row.className = 'admin-video-row';
    row.innerHTML = `
      <div class="admin-row-header">
        <span class="admin-row-title">${video.title}</span>
        <span class="admin-row-filename">${video.filename}</span>
      </div>
      <div class="admin-input-group">
        <input type="text" id="input-${encodeURIComponent(video.filename)}" 
               placeholder="Paste Google Drive / OneDrive share link..." 
               value="${video.onlineUrl || ''}">
        <button class="admin-save-btn" data-filename="${encodeURIComponent(video.filename)}">
          <i class="fa-solid fa-floppy-disk"></i> Save
        </button>
      </div>
      <div class="admin-save-status hidden" id="status-${encodeURIComponent(video.filename)}">Saved successfully!</div>
    `;
    adminVideoList.appendChild(row);
  });

  // Attach event listeners to all save buttons
  adminVideoList.querySelectorAll('.admin-save-btn').forEach(btn => {
    btn.addEventListener('click', async (e) => {
      const filename = decodeURIComponent(e.currentTarget.dataset.filename);
      const input = document.getElementById(`input-${encodeURIComponent(filename)}`);
      const statusEl = document.getElementById(`status-${encodeURIComponent(filename)}`);
      const onlineUrl = input.value.trim();

      // Show saving state
      e.currentTarget.disabled = true;
      statusEl.textContent = 'Saving...';
      statusEl.className = 'admin-save-status';
      statusEl.classList.remove('hidden');

      try {
        const response = await fetch('/api/videos/update-link', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ filename, onlineUrl })
        });

        if (response.ok) {
          statusEl.textContent = 'Link saved successfully!';
          statusEl.className = 'admin-save-status success';
          
          // Update local videos array
          const videoIdx = videos.findIndex(v => v.filename === filename);
          if (videoIdx !== -1) {
            videos[videoIdx].onlineUrl = onlineUrl;
            // Re-render main video grid in case details updated
            renderGrid();
          }
        } else {
          throw new Error('Server returned an error');
        }
      } catch (err) {
        console.error('Failed to save link:', err);
        statusEl.textContent = 'Failed to save link. Try again.';
        statusEl.className = 'admin-save-status error';
      } finally {
        e.currentTarget.disabled = false;
        setTimeout(() => {
          statusEl.classList.add('hidden');
        }, 3000);
      }
    });
  });
}

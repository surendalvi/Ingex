// Global State
let videos = [];
let activeVideo = null;
let currentCategory = 'all';
let searchQuery = '';
let isAdmin = false;

// Determine if running locally or on server
const isLocal = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';

// DOM Elements
const videosGrid = document.getElementById('videos-grid');
const mainVideo = document.getElementById('main-video');
const mainIframe = document.getElementById('main-iframe');
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
const adminBtn = document.getElementById('admin-btn');
const adminModal = document.getElementById('admin-modal');
const closeAdminBtn = document.getElementById('close-admin-btn');
const adminVideoList = document.getElementById('admin-video-list');

// Login modal elements
const loginModal = document.getElementById('login-modal');
const closeLoginBtn = document.getElementById('close-login-btn');
const loginForm = document.getElementById('login-form');
const loginUsernameInput = document.getElementById('login-username');
const loginPasswordInput = document.getElementById('login-password');
const loginError = document.getElementById('login-error');

// Logout button
const adminLogoutBtn = document.getElementById('admin-logout-btn');

// File upload elements
const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file-input');
const browseBtn = document.getElementById('browse-btn');
const uploadProgressContainer = document.getElementById('upload-progress-container');
const uploadFilename = document.getElementById('upload-filename');
const uploadPercent = document.getElementById('upload-percent');
const uploadProgressBar = document.getElementById('upload-progress-bar');
const uploadStatus = document.getElementById('upload-status');

// Add cloud link elements
const addLinkInput = document.getElementById('add-link-input');
const addLinkBtn = document.getElementById('add-link-btn');
const addLinkStatus = document.getElementById('add-link-status');

// Initialize App
document.addEventListener('DOMContentLoaded', () => {
  fetchVideos();
  setupEventListeners();
  checkAdminStatus();
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



  // Admin Modal Open/Close (triggers login if not logged in)
  adminBtn.addEventListener('click', () => {
    if (isAdmin) {
      adminModal.classList.remove('hidden');
      renderAdminList();
    } else {
      loginModal.classList.remove('hidden');
      loginUsernameInput.focus();
    }
  });

  closeAdminBtn.addEventListener('click', () => adminModal.classList.add('hidden'));
  adminModal.addEventListener('click', (e) => {
    if (e.target === adminModal) {
      adminModal.classList.add('hidden');
    }
  });

  // Login Modal close listeners
  closeLoginBtn.addEventListener('click', () => {
    loginModal.classList.add('hidden');
    loginError.classList.add('hidden');
    loginForm.reset();
  });
  loginModal.addEventListener('click', (e) => {
    if (e.target === loginModal) {
      loginModal.classList.add('hidden');
      loginError.classList.add('hidden');
      loginForm.reset();
    }
  });

  // Handle ESC key to close all modals
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      adminModal.classList.add('hidden');
      loginModal.classList.add('hidden');
      loginError.classList.add('hidden');
      loginForm.reset();
    }
  });

  // Login Form submit handler
  loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const username = loginUsernameInput.value.trim();
    const password = loginPasswordInput.value;
    loginError.classList.add('hidden');

    try {
      const response = await fetch('/api/admin/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
      });

      const data = await response.json();
      if (response.ok && data.success) {
        isAdmin = true;
        loginModal.classList.add('hidden');
        loginForm.reset();
        updateAdminButtonUI();
        adminModal.classList.remove('hidden');
        renderAdminList();
      } else {
        loginError.textContent = data.error || 'Invalid credentials';
        loginError.classList.remove('hidden');
      }
    } catch (err) {
      console.error('Login error:', err);
      loginError.textContent = 'Network error. Try again.';
      loginError.classList.remove('hidden');
    }
  });

  // Logout button handler
  adminLogoutBtn.addEventListener('click', async () => {
    try {
      const response = await fetch('/api/admin/logout', { method: 'POST' });
      if (response.ok) {
        isAdmin = false;
        adminModal.classList.add('hidden');
        updateAdminButtonUI();
        fetchVideos(); // Refresh videos list
      } else {
        alert('Logout failed.');
      }
    } catch (err) {
      console.error('Logout error:', err);
    }
  });

  // Drag and drop file upload handlers
  browseBtn.addEventListener('click', () => fileInput.click());
  fileInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
      handleFileUpload(e.target.files[0]);
    }
  });

  ['dragenter', 'dragover'].forEach(eventName => {
    dropZone.addEventListener(eventName, (e) => {
      e.preventDefault();
      e.stopPropagation();
      dropZone.classList.add('dragover');
    }, false);
  });

  ['dragleave', 'dragend', 'drop'].forEach(eventName => {
    dropZone.addEventListener(eventName, (e) => {
      e.preventDefault();
      e.stopPropagation();
      dropZone.classList.remove('dragover');
    }, false);
  });

  dropZone.addEventListener('drop', (e) => {
    const dt = e.dataTransfer;
    const files = dt.files;
    if (files.length > 0) {
      handleFileUpload(files[0]);
    }
  }, false);

  // Add video link button handler
  addLinkBtn.addEventListener('click', async () => {
    const linkInput = addLinkInput.value.trim();
    if (!linkInput) {
      showAddLinkStatus('Error: Please enter a link or iframe code.', 'error');
      return;
    }

    addLinkBtn.disabled = true;
    showAddLinkStatus('Processing cloud video link...', 'info');

    try {
      const response = await fetch('/api/videos/add-by-link', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ linkInput })
      });

      const data = await response.json();
      if (response.ok && data.success) {
        showAddLinkStatus(`Success: ${data.message}`, 'success');
        addLinkInput.value = '';
        setTimeout(() => {
          addLinkStatus.classList.add('hidden');
        }, 4000);
        // Refresh videos list
        await fetchVideos();
        renderAdminList();
      } else {
        showAddLinkStatus(`Error: ${data.error || 'Failed to add video link.'}`, 'error');
      }
    } catch (err) {
      console.error('Add video link error:', err);
      showAddLinkStatus('Error: Network error occurred.', 'error');
    } finally {
      addLinkBtn.disabled = false;
    }
  });

  // Click logo to reset view and clear video parameter (acts as Home button)
  const logoBtn = document.getElementById('logo-btn');
  if (logoBtn) {
    logoBtn.addEventListener('click', () => {
      activeVideo = null;
      mainVideo.classList.add('hidden');
      mainVideo.src = '';
      mainIframe.classList.add('hidden');
      mainIframe.src = 'about:blank';
      playerPlaceholder.classList.remove('hidden');
      
      // Reset details panel
      activeTitle.textContent = 'Select a Demo Video';
      activeDescription.textContent = 'Choose from the grid below to view live demonstrations of Ingenero\'s Agentic AI applications, Process Optimizers, and Operational Dashboards.';
      activeTags.innerHTML = '<span class="category-tag">Industrial AI</span>';
      activeSize.innerHTML = `<i class="fa-solid fa-hard-drive"></i> -- MB`;
      activeDate.innerHTML = `<i class="fa-solid fa-calendar-days"></i> --`;
      copyLinkBtn.setAttribute('disabled', 'true');
      
      // Reset URL to base
      const baseUrl = window.location.origin + window.location.pathname;
      window.history.replaceState({ path: baseUrl }, '', baseUrl);
      
      // Reset grid highlights
      document.querySelectorAll('.video-card').forEach(card => {
        card.classList.remove('active-card');
        card.style.borderColor = '';
        card.style.boxShadow = '';
      });
      
      // Smooth scroll back to top explorer grid
      const explorerElement = document.querySelector('.explorer-section');
      if (explorerElement) {
        explorerElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
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
      selectVideo(video, false); // select, do not scroll on initial load
      
      // Smooth scroll to player on load if deep linked
      const playerElement = document.querySelector('.hero-showcase');
      if (playerElement) {
        playerElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }
  }
}

// Check if URL is an iframe embed source (Google Drive only)
function isEmbedSource(url) {
  if (!url) return false;
  return url.includes('drive.google.com');
}

// Convert sharing and embed links to direct streams for native playback
function getDirectStreamUrl(url) {
  if (!url) return '';
  
  // OneDrive Personal
  if (url.includes('onedrive.live.com')) {
    if (!url.includes('download')) {
      if (url.includes('redir?')) {
        return url.replace('redir?', 'download?');
      }
      if (url.includes('embed?')) {
        return url.replace('embed?', 'download?');
      }
    }
    return url;
  }
  
  // OneDrive Business / SharePoint (Share links and Embed links)
  if (url.includes('sharepoint.com') || url.includes('onedrive.com')) {
    if (url.includes('embed.aspx')) {
      // Convert embed.aspx to download.aspx for direct native streaming
      return url.replace('embed.aspx', 'download.aspx');
    }
    
    // For sharing links (containing /:v:/g/ or standard share query parameter)
    if (!url.includes('download=1')) {
      const separator = url.includes('?') ? '&' : '?';
      return `${url}${separator}download=1`;
    }
  }
  
  return url;
}

// Convert OneDrive and Google Drive share URLs to embed preview URLs
function getEmbedUrl(url) {
  if (!url) return '';
  
  // Google Drive
  if (url.includes('drive.google.com')) {
    let fileId = '';
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
      return `https://drive.google.com/file/d/${fileId}/preview`;
    }
  }

  // OneDrive (Personal)
  if (url.includes('onedrive.live.com')) {
    if (url.includes('/embed')) {
      return url;
    }
    if (url.includes('redir?')) {
      return url.replace('redir?', 'embed?');
    }
    return url;
  }

  // SharePoint / OneDrive Business (already pasted as embed or sharing link)
  if (url.includes('sharepoint.com') || url.includes('onedrive.com')) {
    return url;
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

  const url = video.onlineUrl && video.onlineUrl.trim() !== "" ? video.onlineUrl : video.localUrl;
  
  if (isEmbedSource(url)) {
    // Hide native video player, show iframe
    mainVideo.classList.add('hidden');
    mainVideo.src = '';
    
    mainIframe.src = getEmbedUrl(url);
    mainIframe.classList.remove('hidden');
  } else {
    // Hide iframe, show native video player
    mainIframe.classList.add('hidden');
    mainIframe.src = 'about:blank';
    
    const playUrl = getDirectStreamUrl(url);
    mainVideo.src = playUrl;
    mainVideo.classList.remove('hidden');
    mainVideo.load();
    mainVideo.play().catch(e => {
      console.log('Autoplay was prevented by browser security. User must click play.', e);
    });
  }

  // Update browser URL query parameter without page reload
  const baseUrl = window.location.origin + window.location.pathname;
  const newUrl = `${baseUrl}?video=${encodeURIComponent(video.filename)}`;
  window.history.replaceState({ path: newUrl }, '', newUrl);

  // Swap placeholder
  playerPlaceholder.classList.add('hidden');
  
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
    // Hide from main grid if unlisted/hidden, EXCEPT if it is the currently active video (loaded via direct link)
    if (video.hidden && (!activeVideo || activeVideo.filename !== video.filename)) {
      return false;
    }

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

// Check if user is logged in as admin
async function checkAdminStatus() {
  try {
    const response = await fetch('/api/admin/check');
    if (response.ok) {
      const data = await response.json();
      isAdmin = data.loggedIn;
      updateAdminButtonUI();
      adminBtn.classList.remove('hidden');
    } else {
      adminBtn.classList.add('hidden');
    }
  } catch (err) {
    console.error('Failed to check admin status', err);
    isAdmin = false;
    adminBtn.classList.add('hidden');
  }
}

// Update admin button UI based on login status
function updateAdminButtonUI() {
  if (isAdmin) {
    adminBtn.innerHTML = '<i class="fa-solid fa-gear"></i> Admin Dashboard';
  } else {
    adminBtn.innerHTML = '<i class="fa-solid fa-lock"></i> Admin Portal';
  }
}

// File Upload functionality with progress bar
function handleFileUpload(file) {
  const allowedExtensions = ['.mp4', '.webm', '.ogg', '.mov'];
  const ext = file.name.substring(file.name.lastIndexOf('.')).toLowerCase();
  
  if (!allowedExtensions.includes(ext)) {
    showUploadStatus('Error: Only video files (.mp4, .webm, .ogg, .mov) are allowed.', 'error');
    return;
  }

  if (file.size > 500 * 1024 * 1024) {
    showUploadStatus('Error: Video file exceeds the 500MB size limit.', 'error');
    return;
  }

  // Show progress
  uploadProgressContainer.classList.remove('hidden');
  uploadFilename.textContent = file.name;
  uploadProgressBar.style.width = '0%';
  uploadPercent.textContent = '0%';
  showUploadStatus('Uploading video file...', 'info');

  const formData = new FormData();
  formData.append('video', file);

  const xhr = new XMLHttpRequest();
  xhr.open('POST', '/api/videos/upload', true);

  xhr.upload.addEventListener('progress', (e) => {
    if (e.lengthComputable) {
      const percent = Math.round((e.loaded / e.total) * 100);
      uploadProgressBar.style.width = `${percent}%`;
      uploadPercent.textContent = `${percent}%`;
    }
  });

  xhr.onreadystatechange = () => {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        showUploadStatus('Success: Video uploaded and added to library!', 'success');
        fileInput.value = '';
        setTimeout(() => {
          uploadProgressContainer.classList.add('hidden');
          uploadStatus.classList.add('hidden');
        }, 4000);
        // Refresh videos lists
        fetchVideos().then(() => {
          if (adminModal.classList.contains('hidden') === false) {
            renderAdminList();
          }
        });
      } else {
        let errorMsg = 'Upload failed.';
        try {
          const res = JSON.parse(xhr.responseText);
          errorMsg = res.error || errorMsg;
        } catch(e) {}
        showUploadStatus(`Error: ${errorMsg}`, 'error');
      }
    }
  };

  xhr.send(formData);
}

function showUploadStatus(msg, type) {
  uploadStatus.textContent = msg;
  uploadStatus.className = 'admin-save-status';
  if (type === 'success') uploadStatus.classList.add('success');
  else if (type === 'error') uploadStatus.classList.add('error');
  uploadStatus.classList.remove('hidden');
}

function showAddLinkStatus(msg, type) {
  addLinkStatus.textContent = msg;
  addLinkStatus.className = 'admin-save-status';
  if (type === 'success') addLinkStatus.classList.add('success');
  else if (type === 'error') addLinkStatus.classList.add('error');
  addLinkStatus.classList.remove('hidden');
}

// Render Admin Panel list with full inputs for each video
function renderAdminList() {
  adminVideoList.innerHTML = '';
  
  if (videos.length === 0) {
    adminVideoList.innerHTML = '<p style="color: var(--text-muted); text-align: center;">No videos available to manage.</p>';
    return;
  }

  videos.forEach(video => {
    const card = document.createElement('div');
    card.className = 'admin-video-row';
    card.dataset.filename = video.filename;
    
    // Check which category is selected
    const categories = ['Agentic AI', 'Optimizers', 'Dashboards', 'Demos'];
    let categoryOptions = '';
    categories.forEach(cat => {
      const isSelected = video.category === cat ? 'selected' : '';
      categoryOptions += `<option value="${cat}" ${isSelected}>${cat === 'Demos' ? 'General Demos' : cat}</option>`;
    });

    card.innerHTML = `
      <div class="admin-row-header">
        <span class="admin-row-title">${video.title}</span>
        <span class="admin-row-filename">${video.filename}</span>
      </div>
      
      <div class="admin-edit-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 0.75rem; width: 100%;">
        <div class="form-group">
          <label class="admin-field-label">Title</label>
          <input type="text" class="admin-edit-title" value="${video.title}" placeholder="Video Title">
        </div>
        <div class="form-group">
          <label class="admin-field-label">Category</label>
          <select class="admin-edit-category">
            ${categoryOptions}
          </select>
        </div>
        <div class="form-group" style="grid-column: span 2;">
          <label class="admin-field-label">Cloud Share Link (OneDrive/SharePoint/Google Drive)</label>
          <input type="text" class="admin-edit-url" value="${video.onlineUrl || ''}" placeholder="https://onedrive.live.com/embed?cid=...">
        </div>
        <div class="form-group">
          <label class="admin-field-label">Tags (comma separated)</label>
          <input type="text" class="admin-edit-tags" value="${(video.tags || []).join(', ')}" placeholder="e.g. AI, Process, Chemical">
        </div>
        <div class="form-group">
          <label class="admin-field-label">File Size (MB)</label>
          <input type="number" step="0.01" min="0" class="admin-edit-size" value="${video.sizeBytes ? (video.sizeBytes / (1024 * 1024)).toFixed(2) : ''}" placeholder="e.g. 15.50" ${video.localUrl ? 'disabled title="Calculated automatically from disk"' : ''}>
        </div>
        <div class="form-group" style="grid-column: span 2;">
          <label class="admin-field-label">Description</label>
          <textarea class="admin-edit-description" rows="3" placeholder="Enter video description...">${video.description || ''}</textarea>
        </div>
        <div class="form-group" style="grid-column: span 2; display: flex; align-items: center; gap: 0.5rem; margin-top: 0.25rem;">
          <input type="checkbox" class="admin-edit-hidden" id="hide-${encodeURIComponent(video.filename)}" ${video.hidden ? 'checked' : ''} style="width: auto; margin-right: 0.5rem; cursor: pointer;">
          <label for="hide-${encodeURIComponent(video.filename)}" class="admin-field-label" style="display: inline; text-transform: none; font-weight: 500; cursor: pointer; margin-bottom: 0;">Hide from main library grid (Unlisted, but playable via direct link)</label>
        </div>
      </div>

      <div class="admin-row-actions" style="display: flex; justify-content: space-between; align-items: center; margin-top: 1rem; width: 100%; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 0.75rem;">
        <div>
          <button class="btn btn-secondary btn-sm admin-save-btn" data-filename="${encodeURIComponent(video.filename)}" style="background: var(--accent-blue);">
            <i class="fa-solid fa-floppy-disk"></i> Save Changes
          </button>
          <span class="admin-save-status hidden" id="status-${encodeURIComponent(video.filename)}">Saved!</span>
        </div>
        <button class="btn btn-danger btn-sm admin-delete-btn" data-filename="${encodeURIComponent(video.filename)}">
          <i class="fa-solid fa-trash-can"></i> Delete Video
        </button>
      </div>
    `;
    adminVideoList.appendChild(card);
  });

  // Attach event listeners to all save buttons
  adminVideoList.querySelectorAll('.admin-save-btn').forEach(btn => {
    btn.addEventListener('click', async (e) => {
      const filename = decodeURIComponent(e.currentTarget.dataset.filename);
      const rowEl = e.currentTarget.closest('.admin-video-row');
      const statusEl = document.getElementById(`status-${encodeURIComponent(filename)}`);
      
      const title = rowEl.querySelector('.admin-edit-title').value.trim();
      const category = rowEl.querySelector('.admin-edit-category').value;
      const onlineUrl = rowEl.querySelector('.admin-edit-url').value.trim();
      const tagsString = rowEl.querySelector('.admin-edit-tags').value;
      const description = rowEl.querySelector('.admin-edit-description').value.trim();
      const hidden = rowEl.querySelector('.admin-edit-hidden').checked;
      
      const sizeInput = rowEl.querySelector('.admin-edit-size');
      const sizeMB = sizeInput.value.trim();
      const sizeBytes = sizeMB ? parseFloat(sizeMB) * 1024 * 1024 : 0;

      const tags = tagsString.split(',')
        .map(t => t.trim())
        .filter(t => t.length > 0);

      // Show saving state
      e.currentTarget.disabled = true;
      statusEl.textContent = 'Saving...';
      statusEl.className = 'admin-save-status';
      statusEl.classList.remove('hidden');

      try {
        const response = await fetch('/api/videos/update-metadata', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ filename, title, category, onlineUrl, tags, description, hidden, sizeBytes })
        });

        const data = await response.json();
        if (response.ok && data.success) {
          statusEl.textContent = 'Saved!';
          statusEl.className = 'admin-save-status success';
          
          // Update local videos array and refresh the grid
          const videoIdx = videos.findIndex(v => v.filename === filename);
          if (videoIdx !== -1) {
            videos[videoIdx].title = title;
            videos[videoIdx].category = category;
            videos[videoIdx].onlineUrl = onlineUrl;
            videos[videoIdx].tags = tags;
            videos[videoIdx].description = description;
            videos[videoIdx].hidden = hidden;
            videos[videoIdx].sizeBytes = sizeBytes;
            renderGrid();
            
            // Update the display header in the admin row too
            rowEl.querySelector('.admin-row-title').textContent = title;
          }
        } else {
          throw new Error(data.error || 'Server error');
        }
      } catch (err) {
        console.error('Failed to save metadata:', err);
        statusEl.textContent = 'Save failed. Try again.';
        statusEl.className = 'admin-save-status error';
      } finally {
        e.currentTarget.disabled = false;
        setTimeout(() => {
          statusEl.classList.add('hidden');
        }, 3000);
      }
    });
  });

  // Attach event listeners to delete buttons
  adminVideoList.querySelectorAll('.admin-delete-btn').forEach(btn => {
    btn.addEventListener('click', async (e) => {
      const filename = decodeURIComponent(e.currentTarget.dataset.filename);
      const confirmed = confirm(`Are you sure you want to delete "${filename}" from the server? This will permanently delete the video file from the E:\\Demos directory and clean up its metadata.`);
      
      if (!confirmed) return;

      e.currentTarget.disabled = true;

      try {
        const response = await fetch('/api/videos/delete', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ filename })
        });

        const data = await response.json();
        if (response.ok && data.success) {
          // Refresh list
          await fetchVideos();
          renderAdminList();
          
          // Reset main video view if active video was deleted
          if (activeVideo && activeVideo.filename === filename) {
            document.getElementById('logo-btn').click();
          }
        } else {
          alert(`Failed to delete video: ${data.error || 'Server error'}`);
          e.currentTarget.disabled = false;
        }
      } catch (err) {
        console.error('Delete error:', err);
        alert('Delete failed. Network error.');
        e.currentTarget.disabled = false;
      }
    });
  });
}

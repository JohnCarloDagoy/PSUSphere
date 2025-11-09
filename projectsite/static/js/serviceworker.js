// serviceworker.js

// The cache name — change version when you update static files
const CACHE_NAME = 'projectsite-cache-v1';

// List of URLs and static assets to cache
const urlsToCache = [
  '/',
  '/static/css/bootstrap.min.css',
  '/static/css/ready.css',
  '/static/css/demo.css',
  '/static/js/core/jquery.3.2.1.min.js',
  '/static/js/core/bootstrap.min.js',
  '/static/js/ready.min.js',
];

// Install event — caching static assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('Service Worker: Caching files...');
        return cache.addAll(urlsToCache);
      })
      .catch((err) => console.error('Service Worker cache failed:', err))
  );
});

// Fetch event — serve cached files when offline
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        // Serve from cache if available
        if (response) {
          return response;
        }
        // Otherwise, fetch from network
        return fetch(event.request);
      })
      .catch(() => {
        // Optional: You can return a fallback page/image here
        return caches.match('/');
      })
  );
});

// Activate event — clean up old caches
self.addEventListener('activate', (event) => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (!cacheWhitelist.includes(cacheName)) {
            console.log('Service Worker: Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

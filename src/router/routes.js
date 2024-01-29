
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/HomePage.vue') },
      { path: 'home', component: () => import('pages/HomePage.vue') },
      { path: 'login', component: () => import('pages/LoginPage.vue') },
      { path: 'register', component: () => import('pages/RegistrationPage.vue') },
      { path: 'contacts', component: () => import('pages/MyContactsPage.vue') },
      { path: 'settings', component: () => import('pages/SettingsPage.vue') },
      { path: 'medications', component: () => import('pages/MyMedicationsPage.vue') },
      { path: 'profile', component: () => import('pages/ProfilePage.vue') },
      { path: 'tasks', component: () => import('pages/TasksPage.vue') },
      { path: 'alerts', component: () => import('pages/AlertsPage.vue') },
      { path: 'resources', component: () => import('pages/ResourcesPage.vue') },
      { path: 'timeline', component: () => import('pages/TimelinePage.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes


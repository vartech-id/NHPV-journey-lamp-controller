import { createMemoryHistory, createRouter } from 'vue-router'

// Import all views from the views folder
import CountdownA from '../views/CountdownA.vue'
import CountdownB from '../views/CountdownB.vue'
import DescriptonA from '../views/DescriptonA.vue'
import DescriptonB from '../views/DescriptonB.vue'
import EndPage from '../views/EndPage.vue'
import InfoA from '../views/InfoA.vue'
import InfoB from '../views/InfoB.vue'
import Register from '../views/Register.vue'
import SwicthPage from '../views/SwitchPage.vue'
import Welcome from '../views/Welcome.vue'

const routes = [
  { path: '/', component: Welcome },
  { path: '/countdown-a', component: CountdownA },
  { path: '/countdown-b', component: CountdownB },
  { path: '/description-a', component: DescriptonA },
  { path: '/description-b', component: DescriptonB },
  { path: '/end-page', component: EndPage },
  { path: '/info-a', component: InfoA },
  { path: '/info-b', component: InfoB },
  { path: '/register', component: Register },
  { path: '/switch-page', component: SwicthPage },
  { path: '/welcome', component: Welcome },
]

export const router = createRouter({
  history: createMemoryHistory(),
  routes,
})
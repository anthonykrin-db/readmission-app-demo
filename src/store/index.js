import Vuex from 'vuex'

import connection from './connection'
import survey from './survey'
import auth from './auth'
import patient from './patient'

Vue.use(Vuex)

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

export default function (/* { ssrContext } */) {
  const Store = new Vuex.Store({
    actions: {
      routePage (context, { pageName, url }) {
        console.log('Routing to pageName: ' + pageName + ', returnToUrl: ' + url)
        this.commit('mutateReturnToUrl', url)
        console.log('Getting returnToUrl: ' + this.returnToUrl)
        this.$router.push(pageName).catch(err => {
          // Ignore the vuex err regarding  navigating to the page they are already on.
          if (
            err.name !== 'NavigationDuplicated' &&
            !err.message.includes('Avoided redundant navigation to current location')
          ) {
            // But print any other errors to the console
            console.log('Routing error: ' + err)
          } else {
            console.log('Routing error: ' + err)
          }
        })
      },
      redirect (context) {
        // boilerplate redirect
        var url = this.getReturnToUrl
        console.log('Redirecting: ' + url)
        if (url !== '' && url !== undefined) {
          this.$store.commit('mutateReturnToUrl', '')
          this.$router.push(url)
        } else {
          this.$router.push('/')
        }
      }
    },
    mutations: {
      mutateReturnToUrl (state, url) {
        state.returnToUrl = url
      },
      setModal (state, open) {
        state.modal = open
      },
      setMessage (state, message) {
        state.message = message
      },
      setKeyPressed (state, key) {
        state.keyPressed = key
      }
    },
    getters: {
      showModal: state => {
        return state.showModal
      },
      returnToUrl: state => {
        return state.returnToUrl
      },
      getKeyPressed: state => {
        return state.keyPressed
      }
    },
    modules: {
      connection: connection,
      survey: survey,
      auth: auth,
      patient: patient
    },
    state: {
      modal: false,
      message: '',
      returnToUrl: '',
      serverUrl: '',
      keyPressed: null
    },
    // enable strict mode (adds overhead!)
    // for dev mode only
    strict: process.env.DEV
  })

  return Store
}

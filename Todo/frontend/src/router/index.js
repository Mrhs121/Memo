import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/Login'
import Register from '@/components/Register'
import Main from '@/components/Main'
import Modify from '@/components/Modify'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component:Login 
    },
    {
      path: '/Login',
      name: 'Login',
      component:Login
    },
    {
      path: '/Register',
      name: 'Register',
      component:Register
    },
    {
      path: '/HelloWorld',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/Main',
      name: 'Main',
      component:Main
    },
    {
      path: '/Modify',
      name: 'Modify',
      component:Modify
    }

  ]
})

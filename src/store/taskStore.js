import { defineStore } from 'pinia';
import {axios_client} from '../store/axiosClient';
export const useAuthStore = defineStore('tasks', {
  state: () => ({
    tasks: {}
  }),
  getters: {
    completedTasks(state) {
      var _tasks = []
      // iterate through tasks and if task.complete == true, add to list
      state.tasks.forEach(task => {
        if (task.complete) {
          _tasks.push(task)
        }
      })
      return _tasks
    },
    incompleteTasks(state) {
      var _tasks = []
      // iterate through tasks and if task.complete == false, add to list
      state.tasks.forEach(task => {
        if (!task.complete) {
          _tasks.push(task)
        }
      })
      return _tasks
    },
    createTaskId(state){
      function s4 () {
        return Math.floor((1 + Math.random()) * 0x10000).toString(16).substring(1)
      }
      return s4() + s4() + '-' + s4() + '-' + s4() + '-' + s4() + '-' + s4() + s4() + s4()
    }
  },
  actions: {
    //provided for testing, this would not be appropriate for production
    addTask(context,task){
      this.tasks.push(task)
      return axios_client.post('api/tasks/add', task)
    },
    updateTask (context, task) {
      this.tasks[task.taskId]=task
      return axios_client.post('api/tasks/update', task)
    },
    getTasks (context) {
      return axios_client.get('api/tasks/list')
    }
  }
})

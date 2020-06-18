import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";

Vue.config.productionTip = false;

const low = require("lowdb");
const FileSync = require("lowdb/adapters/FileSync");
const adapter = new FileSync("results.json");
const db = low(adapter);

db.defaults({ results: [] }).write();
Vue.prototype.$db = db;

new Vue({
    vuetify,
    render: (h) => h(App),
}).$mount("#app");

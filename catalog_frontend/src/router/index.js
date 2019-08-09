import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
	routes: [
		{
			path: "/",
			name: "home",
			component: () => import("@/views/Home"),
		}, {
			path: "/login",
			name: "login",
			component: () => import("@/views/Login"),
		}, { // This catches any request not handled above
			path: "*",
			component: () => import("@/views/NotFound"),
		}
	]
});
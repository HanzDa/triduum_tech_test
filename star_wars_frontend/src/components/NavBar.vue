<template>
    <nav
        class="bg-white dark:bg-gray-900 sticky top-0 w-full z-20 border-b border-gray-200 dark:border-gray-600 px-4 py-2 mb-1">
        <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
            <a href="https://flowbite.com/" class="flex items-center">
                <img src="@/assets/logo.png" class="h-8 mr-3" alt="Star wars Logo">
            </a>
            <div class="flex md:order-2">
                <button type="button"
                    class="text-black bg-yellow-300 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center mr-3 md:mr-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                    Login
                </button>

                <button type="button"
                    class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center mr-3 md:mr-0 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                    Sign Up
                </button>
            </div>
            <div class="items-center justify-between hidden w-full md:flex md:w-auto md:order-1" id="navbar-sticky">
                <ul
                    class="flex flex-col p-4 md:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
                    <li>
                        <router-link :to="{ name: 'home' }"
                            class="block py-2 pl-3 pr-4 text-black bg-blue-700 rounded md:bg-transparent md:text-black-700 md:p-0 md:dark:text-blue-500"
                            aria-current="Home">Home</router-link>
                    </li>
                    <li>
                        <router-link :to="{ name: 'about' }"
                            class="block py-2 pl-3 pr-4 text-black bg-blue-700 rounded md:bg-transparent md:text-black-700 md:p-0 md:dark:text-blue-500"
                            aria-current="About">About</router-link>
                    </li>
                    <!-- <li>
                        <router-link :to="{ name='films' }"
                            class="block py-2 pl-3 pr-4 text-white bg-blue-700 rounded md:bg-transparent md:text-blue-700 md:p-0 md:dark:text-blue-500"
                            aria-current="Films"></router-link>
                    </li> -->
                </ul>
            </div>
        </div>
    </nav>
</template>
<script>
export default {

}
</script>
<style></style>
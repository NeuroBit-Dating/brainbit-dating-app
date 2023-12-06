/*window.addEventListener("load", load_page);

function load_page(){
    const profile_content = document.getElementById("profile-content");
    const profile_window = document.getElementById("profile-window");
    const profile_window_content = document.getElementById("profile-window-content");
    const profile_title = document.getElementById("profile-content-title");
    const sidebar_links = document.querySelectorAll(".sidebar_link");

    for (var x in sidebar_links){
        sidebar_links[x].addEventListener("click", displayFunc(sidebar_links[x].textContent));
    }
    function displayFunc(name){
        alert(name);
    }
}*/

const profile_content = document.getElementById("profile-content");
const profile_window = document.getElementById("profile-window");
const profile_window_content = document.getElementById("profile-window-content");
const profile_title = document.getElementById("profile-content-title");

function changePage(name){
    profile_title.textContent = name;
}


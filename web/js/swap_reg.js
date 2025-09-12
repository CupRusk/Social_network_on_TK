let mode_register = true;
let title_in_top = document.querySelector(".title_top");
let input_pass = document.querySelector("#pass");
let input_nick = document.querySelector("#nick");

document.querySelector("#register_block").addEventListener("click", function() {
    if (mode_register) {
        title_in_top.textContent = "Sign in";
        input_nick.setAttribute("name", "nick_sign");
        input_pass.setAttribute("name", "pass_sign");
        mode_register = false;
    } else {
        title_in_top.textContent = "Register";
        input_nick.setAttribute("name", "nick_register");
        input_pass.setAttribute("name", "pass_register");
        mode_register = true;
    }
});

const messages = document.querySelectorAll(".msg");

messages.forEach((message) => {
    setTimeout(() => {

        message.classList.add("msg--hide");

        message.addEventListener("transitionend", () => {
            // message.parentElement.remove();
        });

    }, 5000);
});
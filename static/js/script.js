if (document.body.classList.contains('create-account-page')) {
    document.getElementById('username').addEventListener('focus', function() {
        if (this.value === '') {
            this.placeholder = '';
        }
    });

    document.getElementById('username').addEventListener('blur', function() {
        if (this.value === '') {
            this.placeholder = 'Create a Username';
        }
    });

    document.getElementById('password').addEventListener('focus', function() {
        if (this.value === '') {
            this.placeholder = '';
        }
    });

    document.getElementById('password').addEventListener('blur', function() {
        if (this.value === '') {
            this.placeholder = 'Create a Password';
        }
    });
}

if (document.body.classList.contains('starting-page')) {
    document.getElementById('username').addEventListener('focus', function() {
        if (this.value === '') {
            this.placeholder = '';
        }
    });

    document.getElementById('username').addEventListener('blur', function() {
        if (this.value === '') {
            this.placeholder = 'Username';
        }
    });

    document.getElementById('password').addEventListener('focus', function() {
        if (this.value === '') {
            this.placeholder = '';
        }
    });

    document.getElementById('password').addEventListener('blur', function() {
        if (this.value === '') {
            this.placeholder = 'Password'; 
        }
    });
}

document.getElementById("loginForm").addEventListener("submit", function(event) { 
    var username = document.getElementById("username").value;
    document.cookie = "username=" + username + "; path=/";
});

   function getCookie(name) {
    var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
    if (match) return match[2];
}

var username = getCookie("username");

if (username) {
    var greetingMessage = document.getElementById("greetingMessage");
    greetingMessage.textContent = "Hello " + username + ", welcome back!";
}

if (document.cookie.indexOf("loggedIn=true") === -1 && window.location.pathname !== "/login") {
    window.location.href = "/login";
}

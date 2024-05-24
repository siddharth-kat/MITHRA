
    var users = [
        { username: '2422281'},
        { username: '2422282'},
        { username: '2422283'},
        { username: '2422284'},
        { username: '2422285'},
        { username: '2422286'},
        { username: '2422287'},
        { username: '2422288'},
        { username: '2422289'},
        { username: '2422290'},
        { username: '2422291'},
        { username: '2422292'},
        { username: '2422293'},
        { username: '2422294'},
        { username: '2422295'},
        { username: '2422296'},
        { username: '2422297'},
        { username: '2422298'},
        { username: '2422299'},
        { username: '2422300'},
        { username: '2422301'},
        { username: '2422302'},
        { username: '2422303'},
        { username: '2422304'},
        { username: '2422305'},
        { username: '2422306'},
        { username: '2422307'},
        { username: '2422308'},
        { username: '2422309'},
        { username: '2422310'},
        { username: '2422311'},
        { username: '2422312'},
        { username: '2422313'},
        { username: '2422314'},
        { username: '2422315'},
        { username: '2422316'},
        { username: '2422317'},
        { username: '2422318'},
        { username: '2422319'},
        { username: '2422320'},
        { username: '2422321'},
        { username: '2422322'},
        { username: '2422323'},
        { username: '2422324'},
        { username: '2422325'},
        { username: '2422326'},
        { username: '2422327'},
        { username: '2422328'},
        { username: '2422329'},
        { username: '2422330'},
        { username: '2422331'},
        { username: '2422332'},
        { username: '2422333'},
        { username: '2422334'},
        { username: '2422335'},
        { username: '2422336'},
        { username: '2422337'},
        { username: '2422338'},
        { username: '2422339'},
        { username: '2422340'},
        { username: '2422341'},
        { username: '2422342'},
        { username: '2422343'},
        { username: '2422344'},
        { username: '2422345'},
        { username: '2422346'},
        { username: '2422347'}
    ];
    function login() {
        var username = document.getElementById("username").value;
        var loggedInUser = users.find(function(user) {return user.username === username ;});
        var message=document.getElementById("message");

        if (loggedInUser) {
            // Redirect to the dashboard page
            window.location.href = "home.html";
            
        } else {
            // Display error message
            var errorMessage = document.getElementById("errorMessage");
            errorMessage.innerHTML = "Invalid Netra ID";
            
        }
    }
  

        var loadFile = function(event) {
        var pic = document.getElementById('output');
        pic.src = URL.createObjectURL(event.target.files[0]);
        };

        function Back() {
            window.history.back();
        }

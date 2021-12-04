function change(){
    var submit = document.getElementById('submitbutton');
    submit.style.pointerEvents = "auto";
    submit.style.opacity = 1.0;
};

function loadFile(input) {
    var file = input.files[0];
    var name = document.getElementById('fileName');
    change();
    name.textContent = file.name;

};

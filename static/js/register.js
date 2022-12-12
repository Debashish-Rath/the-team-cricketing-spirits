let name = document.getElementById('name')
let role = document.getElementById('roles')
let role_info = document.getElementById('role-info')
let availability = document.getElementById('availability')
let bat = document.getElementById('bat')
let bowl = document.getElementById('bowl')


console.log(name)
console.log(role)
console.log(role_info)
console.log(availability)

$(document).on('ready', function () {

    $(role).on('change', function () {
        var el = $(this);
        if (el.val() === "Batting") {
            $(role_info).append("<option>Left Hand Bat</option>");
            $(role_info).append("<option>Right Hand Bat</option>");
        } else if (el.val() === "Bowling") {
            $(role_info).append("<option>Left Hand Bowl</option>");
            $(role_info).append("<option>Right Hand Bowl</option>");
        }
    });

});
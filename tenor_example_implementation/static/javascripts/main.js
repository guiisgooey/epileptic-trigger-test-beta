$(function() {
    $('#searchInput').val(window.location.search.split('?search=')[1].replace('+', ' '))
})

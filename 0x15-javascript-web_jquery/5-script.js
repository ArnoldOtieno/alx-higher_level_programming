// adding a li element to a list
$('DIV#add_item').click(function (){
    let element = '<li>Item</li>';
    $('UL.my_list').append(element);
});
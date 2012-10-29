/**
 * Created with PyCharm.
 * User: eysenck
 * Date: 26/10/12
 * Time: 12:16 AM
 * To change this template use File | Settings | File Templates.
 */
$(document).ready(function () {
    var is = 3;
    $('#agregar').click(function () {
        if (is < 6) {
            $('#i' + is).show(1000);
            is += 1;
            if (is > 5) {
                $('#agregar').hide();
            }
        }
        return false;
    });

    $('.x').click(function () {
        if (is > 5) {
            $('#agregar').show();
        }
        var parent = $(this).parent();
        parent.hide();
        is -= 1;
    });
});
<section>
    <div class="container">
        <br><br>
        <div class="row">
            <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                <div class="item-thumbs" style="width: 100%; float: left; position: relative;">
                    <img src="img/works/forms-links-header.jpg" alt="">
                    <h4>Enlaces</h4>
                    <ul id = "enlaces">
                    </ul>
                </div>
            </div>
        </div>
    </div>
</section>

<footer id="pie">
</footer>
</div>


<script type="text/javascript">

function leeMySQL() {
    var grupo = '';
    $.ajax({
        url: "http://interaccionesvih.com:12419/api/enllacos/",
        type: "GET",
        dataType: "jsonp",
        success: function (data) {
            $.each(data, function (index, item) {
                    if (grupo != item.NOM_TIPUS_ENLLAC) {
                        $("#enlaces").append('<li><a href="' + item.ADRECA + '" target="_blank"><H3>' + item.NOM_TIPUS_ENLLAC + '</H3></a>');
                        grupo = item.NOM_TIPUS_ENLLAC;
                    }

                    $("#enlaces").append('<li><a href="' + item.ADRECA + '" target="_blank">' + item.DESCRIPCIO_ENLLAC + '</a>');
                }
            )
        }
    })
}

function cargaPie() {
    $("#pie").load('peu.html');
}
$(document).ready(cargaPie);
$(document).ready(leeMySQL);

</script>

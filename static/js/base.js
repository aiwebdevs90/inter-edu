<script>
    //To show and hide between english and arabic
    $(document).ready(function () {
        $(".switch input").on("change", function (e) {
            const isOn = e.currentTarget.checked;
            if (isOn) {
                $(".contentArabic").show();
                $(".contentEnglish").hide();
            } else {
                $(".contentEnglish").show();
                $(".contentArabic").hide();
            }
        });
    });
</script>
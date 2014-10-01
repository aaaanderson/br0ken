<?php
  $favorite=$_GET["favorite"];
  include($favorite . ".php");
?>

<html>
Favorite anime received.</b>
<?php displayanime(); ?>
</html>

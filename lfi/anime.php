<?php
  $favorite=$_GET["favorite"];
  include($favorite . ".php");
?>

<html>
Favorite anime received.<br/>
<?php displayanime(); ?>
</html>

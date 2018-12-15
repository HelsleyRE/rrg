# Princess Arch

<!DOCTYPE html>
<html>
<head>
  <meta charset='utf-8' />
  <title>Display a map</title>
  <meta name='viewport' content='initial-scale=1,maximum-scale=1,user-scalable=no' />
  <script src='https://api.tiles.mapbox.com/mapbox-gl-js/v0.49.0/mapbox-gl.js'></script>
  <link href='https://api.tiles.mapbox.com/mapbox-gl-js/v0.49.0/mapbox-gl.css' rel='stylesheet' />
  <style>
    body { margin:0; padding:0; }
    #map { position:absolute; top:0; bottom:0; width:100%; }
  </style>
</head>
<body>

<div id='map'></div>
<script>
mapboxgl.accessToken = 'pk.eyJ1IjoiaGVsc2xleXJlIiwiYSI6ImNqcDM0Ym4wdTBlNHQzcnMwdDRmN3FpdWsifQ.4cypf_JwfOAN9YQJnc42Cw';
const map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/helsleyre/cjp34o3z928ld2rn138vlorx8',
  center: [-83.618460, 37.827250],
  zoom: 16.2
});
</script>

</body>
</html>


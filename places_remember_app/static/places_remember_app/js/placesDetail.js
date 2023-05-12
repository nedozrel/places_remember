main();

async function main() {
  await ymaps3.ready;
  const mapElement = document.getElementById('map');
  const locationCenter = mapElement.dataset.locationCenter.split(',');
  const LOCATION = {
    center: [locationCenter[1], locationCenter[0]],
  };
  const {
    YMap,
    YMapDefaultSchemeLayer,
    YMapDefaultFeaturesLayer,
  } = ymaps3;
  const {YMapDefaultMarker} = await ymaps3.import('@yandex/ymaps3-markers@0.0.1');

  const map = new YMap(mapElement, {
    location: {
      center: LOCATION.center,
      zoom: 15,
      controls: [],
    },
  });

  const marker = new YMapDefaultMarker({
    coordinates: LOCATION.center,
  });

  map.addChild(new YMapDefaultSchemeLayer());
  map.addChild(new YMapDefaultFeaturesLayer());
  map.addChild(marker);
  map.addChild(mapListener);
}
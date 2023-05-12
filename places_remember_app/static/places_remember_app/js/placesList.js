const LOCATION = {
  center: [92.8682610105513, 56.00907512437276],
};

main();

async function main() {
  await ymaps3.ready;
  const form = document.querySelector('.add-place-form');
  const {
    YMap,
    YMapDefaultSchemeLayer,
    YMapDefaultFeaturesLayer,
    YMapListener,
  } = ymaps3;
  const {YMapDefaultMarker} = await ymaps3.import('@yandex/ymaps3-markers@0.0.1');

  const map = new YMap(document.getElementById('map'), {
    location: {
      center: LOCATION.center,
      zoom: 12,
      controls: [],
    },
  });

  const marker = new YMapDefaultMarker({
    coordinates: LOCATION.center,
    draggable: true,
    mapFollowsOnDrag: true,
  });

  const mapClickHandler = (e) => {
    console.log(e);
    if (e?.entity.geometry?.coordinates && e.type === 'hotspot') {
      marker.update({
        coordinates: e.entity.geometry.coordinates,
      });
    }
  };

  const mapListener = new YMapListener({
    layerId: 'any',
    onFastClick: mapClickHandler,
  });

  const addCoordsToInputs = () => {
    const coords = marker.coordinates;
    document.querySelector('.longitude-input').value = coords[0];
    document.querySelector('.latitude-input').value = coords[1];
  };

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    console.log('submit');
    addCoordsToInputs();
    form.submit();
  });

  map.addChild(new YMapDefaultSchemeLayer());
  map.addChild(new YMapDefaultFeaturesLayer());
  map.addChild(marker);
  map.addChild(mapListener);
}

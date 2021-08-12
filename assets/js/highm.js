document.addEventListener('DOMContentLoaded', function () {

    const chart = Highcharts.getJSON('/assets/datanew.json', function (data) {
    Highcharts.mapChart('container2', {
        chart: {
            map: 'countries/uz/uz-all'
        },
        title: {
            text: 'Refrigerator\'s places'
        },
        mapNavigation: {
            enabled: true
        },
        tooltip: {
            headerFormat: '',
            pointFormat: '<b>{point.name}</b><br> {point.district} {point.org_name} <br> Sona: {point.quantity}, Jami: {point.capacity}ton <br>Lat: {point.lat:.2f}, Lon: {point.lon:.2f}'
        },
        colorAxis: {
            min: 0,
            max: 20
        },
        plotOptions: {
            mappoint: {
                cluster: {
                    enabled: true,
                    allowOverlap: false,
                    animation: {
                        duration: 450
                    },
                    layoutAlgorithm: {
                        type: 'grid',
                        gridSize: 70
                    },
                    zones: [{
                        from: 1,
                        to: 4,
                        marker: {
                            radius: 13
                        }
                    }, {
                        from: 5,
                        to: 9,
                        marker: {
                            radius: 15
                        }
                    }, {
                        from: 10,
                        to: 15,
                        marker: {
                            radius: 17
                        }
                    }, {
                        from: 16,
                        to: 20,
                        marker: {
                            radius: 19
                        }
                    }, {
                        from: 21,
                        to: 100,
                        marker: {
                            radius: 21
                        }
                    }]
                }
            }
        },
        series: [{
            name: 'Basemap',
            borderColor: '#A0A0A0',
            nullColor: 'rgba(177, 244, 177, 0.5)',
            showInLegend: false
        }, {
            type: 'mappoint',
            enableMouseTracking: true,
            colorKey: 'clusterPointsAmount',
            name: 'Cities',
            data: data
        }]
    });
});
});

import Chart from 'react-apexcharts'
// import Button from '@mui/material/Button';

import Grid from '@mui/material/Grid';

const SystemStats = () => {

    const stateS = {

        series: [75],
        options: {
            chart: {
                height: 350,
                type: 'radialBar',
                colors: ["#FF0000"],
            },
            plotOptions: {
                radialBar: {
                    hollow: {
                        size: '70%',
                    }
                },
            },
            labels: ['Tank Level'],
        },
    };
    const stateP1 = {

        series: [60],
        options: {
            chart: {
                height: 200,
                type: 'radialBar',
                colors: ["#FF0000"],
            },
            plotOptions: {
                radialBar: {
                    hollow: {
                        size: '70%',
                    }
                },
            },
            labels: ['Plant1 M Sat'],
        },
    };
    const stateP2 = {

        series: [70],
        options: {
            chart: {
                height: 200,
                type: 'radialBar',
                colors: ["#FF0000"],
            },
            plotOptions: {
                radialBar: {
                    hollow: {
                        size: '70%',
                    }
                },
            },
            labels: ['Plant2 M Sat'],
        },
    };
    const stateP3 = {

        series: [75],
        options: {
            chart: {
                height: 200,
                type: 'radialBar',
                colors: ["#FF0000"],
            },
            plotOptions: {
                radialBar: {
                    hollow: {
                        size: '70%',
                    }
                },
            },
            labels: ['Plant3 M Sat'],
        },
    };
    return (
        <>
            <Chart
                options={stateS.options}
                series={stateS.series}
                type="radialBar"
                width={500}
                height={320} />
            <Grid container spacing={1}>
                <Chart
                    options={stateP1.options}
                    series={stateP1.series}
                    type="radialBar"
                    width={200}
                    height={200} />
                <Chart
                    options={stateP2.options}
                    series={stateP2.series}
                    type="radialBar"
                    width={200}
                    height={200} />
                <Chart
                    options={stateP3.options}
                    series={stateP3.series}
                    type="radialBar"
                    width={200}
                    height={200} />
            </Grid>
        </>
    );
}

export default SystemStats;
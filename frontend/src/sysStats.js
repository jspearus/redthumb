
import Chart from 'react-apexcharts'
// import Button from '@mui/material/Button';

const SystemStats = () => {

    const state = {

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
    return (
        <>
            <Chart
                options={state.options}
                series={state.series}
                type="radialBar"
                width={500}
                height={320} />
        </>
    );
}

export default SystemStats;

import Chart from 'react-apexcharts'
import Button from '@mui/material/Button';

const MyChart = () => {

    const state = {
        options: {
            chart: {
                id: 'apexchart-example',
                foreColor: '#ff0000',
            },
            xaxis: {
                categories: ['9hr', '8hr', '7hr', '6hr', '5hr', '4hr', '3hr', '2hr', '1hr', '0hr']
            },
            title: {
                text: 'Plant 1 Water Saturation',
                align: 'left',

            },
        },
        series: [{
            name: 'Water Sat.',
            data: [30, 40, 35, 50, 49, 60, 70, 91, 80, 80]
        }]
    }
    return (
        <>
            <Chart
                options={state.options}
                series={state.series}
                type="line"
                width={500}
                height={320} />
            <Button variant="outlined">Update</Button>
        </>

    );
}


export default MyChart
import './App.css'

import MyChart from './chart'
import SystemStats from './sysStats'
import GetRest from './api'


function App() {

  return (
    <div className="App">
      <div className="conntent">
        <h1>Red Thumb</h1>
        <SystemStats />
        <MyChart />
        <GetRest />
      </div>
    </div>
  )
}

export default App
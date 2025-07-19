import { BrowserRouter, Link, Route, Routes } from 'react-router-dom'
import { VolumesPage } from './pages/VolumesPage'
import { DisksPage } from './pages/DisksPage'
import './index.css'

function App() {
  return (
    <BrowserRouter>
      <div className="p-4 flex space-x-4 border-b mb-4">
        <Link to="/volumes" className="text-blue-600">Volumes</Link>
        <Link to="/disks" className="text-blue-600">Disks</Link>
      </div>
      <div className="p-4">
        <Routes>
          <Route path="/volumes" element={<VolumesPage />} />
          <Route path="/disks" element={<DisksPage />} />
          <Route path="*" element={<VolumesPage />} />
        </Routes>
      </div>
    </BrowserRouter>
  )
}

export default App

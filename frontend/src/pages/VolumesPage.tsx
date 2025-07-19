import { useFetch } from '../hooks/useFetch'
import { Volume } from '../types'
import { VolumeCard } from '../components/VolumeCard'

export function VolumesPage() {
  const { data: volumes, loading } = useFetch<Volume[]>('/volumes')

  if (loading) return <p>Loading...</p>
  if (!volumes) return <p>No data</p>

  return (
    <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
      {volumes.map(v => (
        <VolumeCard key={v.uuid} volume={v} />
      ))}
    </div>
  )
}

import { useFetch } from '../hooks/useFetch'
import { Disk } from '../types'
import { DiskTable } from '../components/DiskTable'

export function DisksPage() {
  const { data: disks, loading } = useFetch<Disk[]>('/disks')

  if (loading) return <p>Loading...</p>
  if (!disks) return <p>No data</p>

  return <DiskTable disks={disks} />
}

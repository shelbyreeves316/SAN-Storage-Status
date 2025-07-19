import { Device, Volume } from '../types'
import { StatusBadge } from './StatusBadge'

export function VolumeCard({ volume }: { volume: Volume }) {
  return (
    <div className="border rounded p-4 shadow-sm space-y-2">
      <h2 className="font-semibold text-lg">{volume.label || volume.uuid}</h2>
      <div className="space-y-1">
        {volume.drives.map(dev => (
          <div key={dev.devid} className="flex items-center justify-between text-sm">
            <span>{dev.path}</span>
            <StatusBadge status={dev.smart.status} />
          </div>
        ))}
      </div>
    </div>
  )
}

import { Disk } from '../types'
import { StatusBadge } from './StatusBadge'

export function DiskTable({ disks }: { disks: Disk[] }) {
  return (
    <table className="min-w-full text-left text-sm">
      <thead>
        <tr>
          <th className="px-2 py-1">Device</th>
          <th className="px-2 py-1">Health</th>
          <th className="px-2 py-1">Temp</th>
        </tr>
      </thead>
      <tbody>
        {disks.map(d => (
          <tr key={d.name} className="border-t">
            <td className="px-2 py-1">{d.name}</td>
            <td className="px-2 py-1"><StatusBadge status={d.smart.status} /></td>
            <td className="px-2 py-1">{d.smart.temperature ?? '--'}&deg;C</td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}

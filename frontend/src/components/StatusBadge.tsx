import clsx from 'clsx'

export function StatusBadge({ status }: { status: string }) {
  const color = status === 'PASSED'
    ? 'bg-green-500'
    : status === 'FAILED'
      ? 'bg-red-500'
      : 'bg-gray-400'

  return (
    <span className={clsx('px-2 py-1 text-xs text-white rounded', color)}>
      {status}
    </span>
  )
}

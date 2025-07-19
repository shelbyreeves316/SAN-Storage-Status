import { useEffect, useState } from 'react'
import { AxiosRequestConfig } from 'axios'
import { api } from '../api/client'

export function useFetch<T = unknown>(url: string, config?: AxiosRequestConfig) {
  const [data, setData] = useState<T | null>(null)
  const [error, setError] = useState<unknown>(null)
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    setLoading(true)
    api.get<T>(url, config)
      .then(res => setData(res.data))
      .catch(err => setError(err))
      .finally(() => setLoading(false))
  }, [url])

  return { data, error, loading }
}

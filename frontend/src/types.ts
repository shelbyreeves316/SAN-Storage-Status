export interface SmartInfo {
  status: string
  alert?: string | null
  temperature?: number | null
}

export interface Device {
  devid: string
  size: string
  used: string
  path: string
  smart: SmartInfo
}

export interface Volume {
  label: string
  uuid: string
  usage?: string
  drives: Device[]
}

export interface Disk {
  name: string
  smart: SmartInfo
}

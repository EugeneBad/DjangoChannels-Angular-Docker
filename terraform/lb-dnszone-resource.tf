resource "google_dns_managed_zone" "main-dnszone" {
  name        = "main-dnszone"
  dns_name    = "djchangular.tk."
  description = "Main DNS zone"
}
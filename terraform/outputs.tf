output "main-ip" {
  value = "${google_compute_global_forwarding_rule.main-gfr.ip_address}"
}

output "main-nameservers" {
  value = "${google_dns_managed_zone.main-dnszone.name_servers}"
}
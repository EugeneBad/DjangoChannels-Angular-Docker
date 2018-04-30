output "main-ip" {
  value = "${google_compute_global_forwarding_rule.main-gfr.ip_address}"
}

output "k8smaster-ip" {
  value = "${google_compute_instance.k8smaster-nat-instance.network_interface.access_config.nat_ip}"
}

output "main-nameservers" {
  value = "${google_dns_managed_zone.main-dnszone.name_servers}"
}
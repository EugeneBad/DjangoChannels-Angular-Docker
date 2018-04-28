resource "google_dns_record_set" "main" {
  name = "${google_dns_managed_zone.main-dnszone.dns_name}"
  managed_zone = "${google_dns_managed_zone.main-dnszone.name}"
  type = "A"
  ttl  = 5

  rrdatas = ["${google_compute_global_forwarding_rule.main-gfr.ip_address}"]
}

resource "google_dns_record_set" "backend" {
  name = "api.${google_dns_managed_zone.main-dnszone.dns_name}"
  managed_zone = "${google_dns_managed_zone.main-dnszone.name}"
  type = "A"
  ttl  = 5

  rrdatas = ["${google_compute_global_forwarding_rule.main-gfr.ip_address}"]
}
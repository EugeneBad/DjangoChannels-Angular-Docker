resource "google_compute_address" "db-address" {
  name = "db-address"
  address_type = "INTERNAL"
  subnetwork = "${google_compute_subnetwork.private-subnetwork.self_link}"
  address = "10.0.2.3"
}
resource "google_compute_address" "db-address" {
  name = "db-address"
  address_type = "INTERNAL"
  subnetwork = "${google_compute_subnetwork.private-subnetwork.self_link}"
  address = "10.0.2.3"
}

resource "google_compute_address" "lb-nat-address" {
  name = "lb-nat-address"
  address_type = "EXTERNAL"
}
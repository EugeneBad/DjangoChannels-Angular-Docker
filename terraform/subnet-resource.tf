resource "google_compute_subnetwork" "private-subnetwork" {
  name          = "private-subnetwork"
  ip_cidr_range = "10.0.2.0/24"
  network       = "${google_compute_network.djchangular-vpc.name}"
  description = "Subnetwork in which the private instances will be created"
}

resource "google_compute_subnetwork" "public-subnetwork" {
  name          = "public-subnetwork"
  ip_cidr_range = "${cidrsubnet("10.0.0.0/16", 8, 0)}"
  network       = "${google_compute_network.djchangular-vpc.name}"
  description = "Subnetwork in which the public instances will be created"
}
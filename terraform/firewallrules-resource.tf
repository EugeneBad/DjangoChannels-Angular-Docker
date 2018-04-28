resource "google_compute_firewall" "allow-public-firewallrule" {
  name    = "allow-public-firewallrule"
  network = "${google_compute_network.djchangular-vpc.name}"
  description = "Firewall rule that opens http port(80) on the public instance"

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
    ports    = ["22", "80", "6443"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags = ["public"]
}

resource "google_compute_firewall" "allow-private-all" {
  name = "allow-private-all"
  network = "${google_compute_network.djchangular-vpc.name}"
  description = "Firewall rule to allow traffic from anywhere on the vpc to the private instances"

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags = ["private"]
}

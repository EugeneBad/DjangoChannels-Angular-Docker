resource "google_compute_autoscaler" "k8sclstr-autoscaler" {
  name   = "k8sclstr-autoscaler"
  zone   = "asia-south1-a"
  target = "${google_compute_instance_group_manager.k8sclstr-ig-manager.self_link}"

  autoscaling_policy = {
    max_replicas    = 3
    min_replicas    = 2
    cooldown_period = 60

    cpu_utilization {
      target = 0.4
    }
  }
}
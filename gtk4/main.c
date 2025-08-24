#include <gtk/gtk.h>

static void
button_clicked (GtkButton *btn)
{
  const gchar *s = gtk_button_get_label (btn);
  if (g_strcmp0 (s, "1") == 0)
    {
      gtk_button_set_label (btn, "2");
    }
  else
    {
      gtk_button_set_label (btn, "1");
    }

  g_print ("Hello World\n");
}

static void
button2_clicked (GtkButton *btn, GtkWindow *win)
{
  gtk_window_destroy (win);
}

static void
activate (GtkApplication *app)
{
  GtkWidget *window = gtk_application_window_new (app);
  gtk_window_set_title (GTK_WINDOW (window), "Reza Cal");
  gtk_window_set_default_size (GTK_WINDOW (window), 400, 300);

  GtkWidget *grid = gtk_grid_new ();
  gtk_window_set_child (GTK_WINDOW (window), grid);

  GtkWidget *label = gtk_label_new ("Reza Mousavi");
  gtk_grid_attach (GTK_GRID (grid), label, 0, 0, 4, 1);

  GtkWidget *entry = gtk_entry_new ();
  gtk_grid_attach (GTK_GRID (grid), entry, 0, 1, 4, 2);

  GtkWidget *button = gtk_button_new_with_label ("1");
  g_signal_connect (button, "clicked", G_CALLBACK (button_clicked), NULL);
  // g_signal_connect_swapped (button, "clicked", G_CALLBACK
  // (gtk_window_destroy), window);
  gtk_grid_attach (GTK_GRID (grid), button, 0, 3, 1, 1);

  GtkWidget *button2 = gtk_button_new_with_label ("2");
  g_signal_connect (button2, "clicked", G_CALLBACK (button2_clicked), window);
  gtk_grid_attach (GTK_GRID (grid), button2, 2, 3, 1, 1);

  gtk_window_present (GTK_WINDOW (window));
}

int
main (int argc, char **argv)
{
  GtkApplication *app
      = gtk_application_new ("reza.calendar", G_APPLICATION_DEFAULT_FLAGS);
  g_signal_connect (app, "activate", G_CALLBACK (activate), NULL);
  int status = g_application_run (G_APPLICATION (app), argc, argv);
  g_object_unref (app);

  return status;
}

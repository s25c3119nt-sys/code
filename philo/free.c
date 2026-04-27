#include "philo.h"

void	destroy_mutex(t_data *d)
{
	int	i;

	i = 0;
	while (i < d->num)
	{
		pthread_mutex_destroy(&d->forks[i]);
		i++;
	}
	pthread_mutex_destroy(&d->print);
	pthread_mutex_destroy(&d->stop_mutex);
	pthread_mutex_destroy(&d->meal_mutex);
}

void	free_all(t_data *d)
{
	if (d->forks)
		free(d->forks);
	if (d->philos)
		free(d->philos);
}

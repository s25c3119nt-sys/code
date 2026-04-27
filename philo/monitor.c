#include "philo.h"

#include "philo.h"

static int	check_dead(t_data *d, int i)
{
	long	last;

	pthread_mutex_lock(&d->meal_mutex);
	last = d->philos[i].last_meal;
	pthread_mutex_unlock(&d->meal_mutex);

	if (ft_time() - last > d->time_die)
	{
		pthread_mutex_lock(&d->print);
		printf("%ld %d died\n",
			ft_time() - d->start,
			d->philos[i].id);
		pthread_mutex_unlock(&d->print);
		set_stop(d, 1);
		return (1);
	}
	return (0);
}

void	*monitor(void *arg)
{
	t_data	*d;
	int		i;

	d = (t_data *)arg;
	while (!get_stop(d))
	{
		i = 0;
		while (i < d->num)
		{
			if (check_dead(d, i))
				return (NULL);
			i++;
		}
		usleep(1000);
	}
	return (NULL);
}

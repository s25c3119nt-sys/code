#include "philo.h"

long	ft_time(void)
{
	struct timeval	tv;

	gettimeofday(&tv, NULL);
	return (tv.tv_sec * 1000 + tv.tv_usec / 1000);
}

int	ft_atoi(const char *s)
{
	int	i;
	int	n;

	i = 0;
	n = 0;
	while (s[i])
	{
		n = n * 10 + (s[i] - '0');
		i++;
	}
	return (n);
}

int	get_stop(t_data *d)
{
	int	val;

	pthread_mutex_lock(&d->stop_mutex);
	val = d->stop;
	pthread_mutex_unlock(&d->stop_mutex);
	return (val);
}

void	set_stop(t_data *d, int val)
{
	pthread_mutex_lock(&d->stop_mutex);
	d->stop = val;
	pthread_mutex_unlock(&d->stop_mutex);
}

void	ft_print(t_philo *p, char *msg)
{
	pthread_mutex_lock(&p->data->print);
	if (!get_stop(p->data))
		printf("%ld %d %s\n",
			ft_time() - p->data->start,
			p->id, msg);
	pthread_mutex_unlock(&p->data->print);
}